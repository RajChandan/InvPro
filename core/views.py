from django.shortcuts import render

def landing_page(request):
    features = [
        {
            "title": "AI-Powered Due Diligence",
            "description": "Advanced algorithms analyze market trends, financial metrics, and growth indicators to provide comprehensive investment insights.",
            "icon": "M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"
        },
        {
            "title": "Exclusive Deal Flow",
            "description": "Access pre-vetted investment opportunities from high-growth startups across technology, healthcare, and emerging sectors.",
            "icon": "M12 6V4m0 2a2 2 0 100 4m0-4a2 2 0 110 4m-6 8a2 2 0 100-4m0 4a2 2 0 110-4m0 4v2m0-6V4m6 6v10m6-2a2 2 0 100-4m0 4a2 2 0 110-4m0 4v2m0-6V4"
        },
        {
            "title": "Secure Transactions",
            "description": "Enterprise-grade security protocols and compliant infrastructure for seamless investment processing.",
            "icon": "M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z"
        },
    ]
    return render(request, 'core/landing.html', {'features': features})
