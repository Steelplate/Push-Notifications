from notificationService import service

push = service("config.yaml")

success = push.notification("Hello World", "test.png")
print(success)
