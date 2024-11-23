from django.core.mail import send_mail
from shop import settings

def send_html_email(subject, to_email, num, region, city, street):
    html_message = f"""
    <html>
    <head>
        <style>
            body {{
                font-family: Arial, sans-serif;
                background-color: #f4f4f4;
                margin: 0;
                padding: 0;
            }}
            .container {{
                width: 100%;
                max-width: 600px;
                margin: auto;
                background: white;
                border-radius: 5px;
                box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            }}
            .header {{
                background: url('your-background-image-url.jpg') no-repeat center center;
                background-size: cover;
                height: 200px;
                text-align: center;
                color: white;
                font-size: 24px;
                padding: 20px;
            }}
            .content {{
                padding: 20px;
                color: #333;
            }}
            .footer {{
                text-align: center;
                padding: 10px;
                font-size: 12px;
                color: #777;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                Приветствуем вас {subject}!
            </div>
            <div class="content">
                <h1>Заказ №{num} оформлен успешно!</h1>
                <p>Адрес доставки:{region}, {city}, {street}</p>
            </div>
            <div class="footer">
                &copy; 2024 MEGA SHOP | Все права защищены
            </div>
        </div>
    </body>
    </html>
    """

    from_email = settings.EMAIL_HOST_USER
    
    send_mail(
        subject,
        '',
        from_email,
        [to_email],
        fail_silently=False,
        html_message=html_message,
    )