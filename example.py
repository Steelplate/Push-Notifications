from notification_service import Service

push = Service("config.yaml")

success = push.notification("Hello World", "test.png")
print(success)
