from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import JsonResponse
from django.contrib import messages
from .models import ContactMessage, InvestmentInquiry, Startup


def landing_page(request):
    features = [
        {
            "title": "AI-Powered Due Diligence",
            "description": "Advanced algorithms analyze market trends, financial metrics, and growth indicators to provide comprehensive investment insights.",
            "icon": "M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2",
        },
        {
            "title": "Exclusive Deal Flow",
            "description": "Access pre-vetted investment opportunities from high-growth startups across technology, healthcare, and emerging sectors.",
            "icon": "M12 6V4m0 2a2 2 0 100 4m0-4a2 2 0 110 4m-6 8a2 2 0 100-4m0 4a2 2 0 110-4m0 4v2m0-6V4m6 6v10m6-2a2 2 0 100-4m0 4a2 2 0 110-4m0 4v2m0-6V4",
        },
        {
            "title": "Secure Transactions",
            "description": "Enterprise-grade security protocols and compliant infrastructure for seamless investment processing.",
            "icon": "M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z",
        },
        {
            "title": "Portfolio Analytics",
            "description": "Real-time monitoring and reporting tools to track portfolio performance and optimize investment strategy.",
            "icon": "M16 8v8m-4-5v5m-4-2v2m-2 4h12a2 2 0 002-2V6a2 2 0 00-2-2H6a2 2 0 00-2 2v12a2 2 0 002 2z",
        },
        {
            "title": "Expert Network",
            "description": "Connect with industry experts, successful founders, and fellow investors for deeper market insights.",
            "icon": "M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 019.288 0",
        },
        {
            "title": "Real-Time Updates",
            "description": "Instant notifications on investment opportunities, market changes, and portfolio performance metrics.",
            "icon": "M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z",
        },
    ]

    steps = [
        {
            "title": "Profile Creation & Verification",
            "description": "Complete your investor profile and verification process. Our platform ensures compliance with accreditation requirements.",
        },
        {
            "title": "Access Deal Flow",
            "description": "Browse through our curated list of pre-vetted startups and receive AI-powered recommendations based on your investment preferences.",
        },
        {
            "title": "Due Diligence",
            "description": "Review comprehensive AI-generated reports, financial metrics, and market analysis for informed decision-making.",
        },
        {
            "title": "Secure Investment",
            "description": "Execute investments through our secure platform with digital documentation and automated compliance checks.",
        },
        {
            "title": "Portfolio Management",
            "description": "Track performance, receive updates, and manage your investment portfolio through our intuitive dashboard.",
        },
    ]
    testimonials = [
        {
            "name": "Sarah Chen",
            "position": "Managing Partner, Beyond Capital",
            "message": "The AI-powered insights have transformed our investment process. We've seen a 40% increase in deal flow quality since using InvestorPro.",
            "initials": "SC",
        },
        {
            "name": "Michael Stern",
            "position": "Founder, TechVentures Capital",
            "message": "The platform's secure transaction infrastructure and comprehensive analytics have made our investment process significantly more efficient.",
            "initials": "MS",
        },
        {
            "name": "Jennifer Wong",
            "position": "CEO, Innovation Capital",
            "message": "InvestorPro's AI-driven due diligence has helped us identify promising startups we might have otherwise missed. Outstanding platform.",
            "initials": "JW",
        },
    ]
    pricing_plans = [
        {
            "name": "Individual",
            "price": "$999",
            "features": [
                "Basic AI-powered insights",
                "Up to 5 active investments",
                "Standard due diligence reports",
            ],
            "button_text": "Get Started",
            "popular": False,
        },
        {
            "name": "Professional",
            "price": "$2,499",
            "features": [
                "Advanced AI analytics",
                "Up to 15 active investments",
                "Premium due diligence reports",
                "Priority deal access",
            ],
            "button_text": "Get Started",
            "popular": True,
        },
        {
            "name": "Enterprise",
            "price": "Custom",
            "features": [
                "Custom AI solutions",
                "Unlimited investments",
                "Dedicated investment advisor",
                "Custom API integration",
            ],
            "button_text": "Contact Sales",
            "popular": False,
        },
    ]
    statistics = [
        {
            "value": "5%",
            "label": "Total Investments Facilitated",
            "icon": "M12 8c-1.657 0-3 .895-3 2s1.343 2 3 2 3 .895 3 2-1.343 2-3 2m0-8c1.11 0 2.08.402 2.599 1M12 8V7m0 1v8m0 0v1m0-1c-1.11 0-2.08-.402-2.599-1M21 12a9 9 0 11-18 0 9 9 0 0118 0z",
        },
        {
            "value": "1000%",
            "label": "Active Investors",
            "icon": "M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 019.288 0M15 7a3 3 0 11-6 0 3 3 0 016 0zm6 3a2 2 0 11-4 0 2 2 0 014 0zM7 10a2 2 0 11-4 0 2 2 0 014 0z",
        },
        {
            "value": "500%",
            "label": "Vetted Startups",
            "icon": "M19 21V5a2 2 0 00-2-2H7a2 2 0 00-2 2v16m14 0h2m-2 0h-5m-9 0H3m2 0h5M9 7h1m-1 4h1m4-4h1m-1 4h1m-5 10v-5a1 1 0 011-1h2a1 1 0 011 1v5m-4 0h4",
        },
        {
            "value": "98%",
            "label": "Success Rate",
            "icon": "M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z",
        },
    ]

    # Add contact_success parameter from GET to the context.
    context = {
        "features": features,
        "steps": steps,
        "testimonials": testimonials,
        "pricing_plans": pricing_plans,
        "statistics": statistics,
    }

    if request.method == "POST":
        # Retrieve form data
        name = request.POST.get("name", "").strip()
        email = request.POST.get("email", "").strip()
        company = request.POST.get("company", "").strip()
        phone = request.POST.get("phone", "").strip()
        organization_type = request.POST.get("organization_type", "").strip()
        message_text = request.POST.get("message", "").strip()
        print(
            request.META.get("HTTP_X_REQUESTED_WITH"),
            " ========== request header",
        )
        # Basic validation
        if not name or not email or not message_text:
            error_msg = "Required fields are empty"
            if request.META.get("HTTP_X_REQUESTED_WITH") == "XMLHttpRequest":
                return JsonResponse(
                    {"status": "error", "message": error_msg}, status=400
                )
            else:
                context["contact_error"] = error_msg
                return render(request, "core/landing.html", context)
        else:
            # Save contact message into DB
            contact_message = ContactMessage(
                name=name,
                email=email,
                company=company,
                phone=phone,
                organization_type=organization_type,
                message=message_text,
            )
            contact_message.save()
            success_msg = (
                "Thank you for contacting us. We will get back to you shortly."
            )
            if request.META.get("HTTP_X_REQUESTED_WITH") == "XMLHttpRequest":
                return JsonResponse({"status": "success", "message": success_msg})
            else:
                return redirect(reverse("landing_page"))

    return render(request, "core/landing.html", context)


def start_investing(request):
    context = {}

    if request.method == "POST":
        name = request.POST.get("name", "").strip()
        email = request.POST.get("email", "").strip()
        phone = request.POST.get("phone", "").strip()
        investment_amount = request.POST.get("investment_amount", "").strip()
        investment_goal = request.POST.get("investment_goal", "").strip()
        risk_tolerance = request.POST.get("risk_tolerance", "").strip()
        sectors = request.POST.get("sectors", "").strip()

        # Basic validation: Name, Email, Investment Amount, and Investment Goal are required.
        if not name or not email or not investment_amount or not investment_goal:
            error_msg = "Please fill in the required fields (Name, Email, Investment Amount, and Investment Goal)."
            if request.META.get("HTTP_X_REQUESTED_WITH") == "XMLHttpRequest":
                return JsonResponse(
                    {"status": "error", "message": error_msg}, status=400
                )
            else:
                context["error"] = error_msg
                return render(request, "core/start_investing.html", context)
        else:
            # Save the inquiry
            inquiry = InvestmentInquiry(
                name=name,
                email=email,
                phone=phone,
                investment_amount=investment_amount,
                investment_goal=investment_goal,
                risk_tolerance=risk_tolerance,
                sectors=sectors,
            )
            inquiry.save()
            success_msg = "Thank you for your interest. We will contact you soon to help you start investing."
            if request.META.get("HTTP_X_REQUESTED_WITH") == "XMLHttpRequest":
                return JsonResponse({"status": "success", "message": success_msg})
            else:
                context["success"] = success_msg
                return render(request, "core/investing.html", context)

    return render(request, "core/investing.html", context)


def register_startup(request):
    if request.method == "POST":
        startup_name = request.POST.get("startup_name", "").strip()
        company_url = request.POST.get("company_url", "").strip()
        email = request.POST.get("email", "").strip()
        description = request.POST.get("description", "").strip()
        phone = request.POST.get("phone", "").strip()
        founder_name = request.POST.get("founder_name", "").strip()
        industry = request.POST.get("industry", "").strip()
        startup_stage = request.POST.get("startup_stage", "").strip()
        if not (
            startup_name
            and company_url
            and email
            and founder_name
            and industry
            and startup_stage
        ):
            messages.error(request, "Please fill in all required fields.")
            return render(request, "core/register_startup.html")

        startup = Startup(
            startup_name=startup_name,
            company_url=company_url,
            email=email,
            phone=phone,
            description=description,
            founder_name=founder_name,
            industry=industry,
            startup_stage=startup_stage,
        )
        startup.save()
        messages.success(request, "Your startup has been registered successfully!")
        return redirect("landing_page")
    return render(request, "core/register_startup.html")
