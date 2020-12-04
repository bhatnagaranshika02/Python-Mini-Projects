from plyer import notification
title = "Hello, I am Anshika..!!!"

message = "Do subscribe to my Youtube channel"

notification.notify(title = title,
                    message = message,
                    app_icon = None,
                    timeout = 10,
                    toast = False)
