import logging
import time
import functools

# Get loggers
logger = logging.getLogger('core')
security_logger = logging.getLogger('core.security')
performance_logger = logging.getLogger('core.performance')

def log_function_call(func):
    """Decorator to log function calls with timing"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        func_name = func.__name__
        logger.debug(f"Calling function: {func_name}")
        
        try:
            result = func(*args, **kwargs)
            execution_time = (time.time() - start_time) * 1000  # Convert to milliseconds
            
            # Log performance metrics if execution time is above threshold
            if execution_time > 100:  # Log if execution takes more than 100ms
                performance_logger.warning(
                    f"Slow function execution: {func_name} took {execution_time:.2f}ms"
                )
            else:
                performance_logger.info(
                    f"Function execution: {func_name} took {execution_time:.2f}ms"
                )
            
            return result
            
        except Exception as e:
            logger.error(f"Error in {func_name}: {str(e)}", exc_info=True)
            raise
    
    return wrapper

def log_security_event(event_type, user=None, ip_address=None, details=None):
    """Log security-related events"""
    event_data = {
        'event_type': event_type,
        'user': str(user) if user else 'anonymous',
        'ip_address': ip_address,
        'details': details or {}
    }
    security_logger.info(f"Security event: {event_data}")

def log_performance_metric(metric_name, value, unit='ms', context=None):
    """Log performance metrics"""
    metric_data = {
        'metric': metric_name,
        'value': value,
        'unit': unit,
        'context': context or {}
    }
    performance_logger.info(f"Performance metric: {metric_data}")

def log_database_query(query, execution_time):
    """Log database query performance"""
    if execution_time > 100:  # Log slow queries (>100ms)
        performance_logger.warning(
            f"Slow database query ({execution_time:.2f}ms): {query}"
        )
    else:
        performance_logger.debug(
            f"Database query ({execution_time:.2f}ms): {query}"
        )

def log_api_request(method, path, status_code, response_time, user=None):
    """Log API request details"""
    api_data = {
        'method': method,
        'path': path,
        'status_code': status_code,
        'response_time': f"{response_time:.2f}ms",
        'user': str(user) if user else 'anonymous'
    }
    logger.info(f"API Request: {api_data}")

def log_error(error, context=None):
    """Log error with context"""
    error_data = {
        'error': str(error),
        'type': type(error).__name__,
        'context': context or {}
    }
    logger.error(f"Error occurred: {error_data}", exc_info=True)

class RequestLogger:
    """Context manager for logging request processing"""
    def __init__(self, request):
        self.request = request
        self.start_time = None
    
    def __enter__(self):
        self.start_time = time.time()
        logger.info(f"Starting request processing: {self.request.method} {self.request.path}")
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        execution_time = (time.time() - self.start_time) * 1000
        if exc_type:
            logger.error(f"Request failed: {self.request.method} {self.request.path}", exc_info=True)
        else:
            logger.info(f"Completed request: {self.request.method} {self.request.path} in {execution_time:.2f}ms") 