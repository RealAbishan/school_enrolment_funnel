from django.db import models

#Model will have the details of the students and the Status

class FunnelStatus(models.Model):
    name = models.CharField(max_length=100, unique=True)
    order = models.PositiveIntegerField()

    def __str__(self):
        return self.name
class Student (models.Model):
    name = models.CharField(max_length=200)
    current_status = models.ForeignKey(FunnelStatus, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name


class StatusLog(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    from_status = models.ForeignKey(FunnelStatus, related_name='from_status', on_delete=models.SET_NULL, null=True)
    to_status = models.ForeignKey(FunnelStatus, related_name='to_status', on_delete=models.SET_NULL, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.name} from {self.from_status} to {self.to_status} at {self.timestamp}"

