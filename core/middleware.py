from django.http import HttpResponse
from django.core.cache import cache
from django.conf import settings
import time
import re

class SecurityMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.rate_limit = 100  # requests per minute
        self.rate_limit_window = 60  # seconds

    def __call__(self, request):
        # Add security headers
        response = self.get_response(request)
        
        # Security Headers
        response['X-Content-Type-Options'] = 'nosniff'
        response['X-Frame-Options'] = 'DENY'
        response['X-XSS-Protection'] = '1; mode=block'
        response['Strict-Transport-Security'] = 'max-age=31536000; includeSubDomains'
        response['Content-Security-Policy'] = "default-src 'self'; script-src 'self' 'unsafe-inline' 'unsafe-eval' https://cdn.jsdelivr.net; style-src 'self' 'unsafe-inline' https://fonts.googleapis.com; font-src 'self' https://fonts.gstatic.com; img-src 'self' data: https:; connect-src 'self' https://api.example.com;"
        response['Referrer-Policy'] = 'strict-origin-when-cross-origin'
        response['Permissions-Policy'] = 'geolocation=(), microphone=(), camera=()'

        # Rate Limiting
        if request.method == 'POST':
            client_ip = self.get_client_ip(request)
            cache_key = f'rate_limit_{client_ip}'
            
            # Get current request count
            request_count = cache.get(cache_key, 0)
            
            # Check if rate limit exceeded
            if request_count >= self.rate_limit:
                return HttpResponse('Rate limit exceeded. Please try again later.', status=429)
            
            # Increment request count
            cache.set(cache_key, request_count + 1, self.rate_limit_window)

        return response

    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip

class InputSanitizationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.xss_patterns = [
            r'<script[^>]*>.*?</script>',
            r'javascript:[^\'"]*',
            r'on\w+\s*=',
            r'data:[^\'"]*',
        ]

    def __call__(self, request):
        # Sanitize GET parameters
        if request.GET:
            request.GET = self.sanitize_dict(request.GET)
        
        # Sanitize POST data
        if request.POST:
            request.POST = self.sanitize_dict(request.POST)
        
        return self.get_response(request)

    def sanitize_dict(self, data_dict):
        sanitized = {}
        for key, value in data_dict.items():
            if isinstance(value, str):
                sanitized[key] = self.sanitize_input(value)
            elif isinstance(value, dict):
                sanitized[key] = self.sanitize_dict(value)
            else:
                sanitized[key] = value
        return sanitized

    def sanitize_input(self, value):
        # Remove XSS patterns
        for pattern in self.xss_patterns:
            value = re.sub(pattern, '', value, flags=re.IGNORECASE)
        
        # HTML encode special characters
        value = value.replace('&', '&amp;')
        value = value.replace('<', '&lt;')
        value = value.replace('>', '&gt;')
        value = value.replace('"', '&quot;')
        value = value.replace("'", '&#x27;')
        
        return value 