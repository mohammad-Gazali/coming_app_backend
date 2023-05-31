from django.db import models



class Massjed(models.Model):

    name = models.CharField(max_length=511)

    hour_value = models.IntegerField()


    def __str__(self) -> str:
        return self.name


class Course(models.Model):
    
    name = models.CharField(max_length=511)

    massjed = models.ForeignKey(Massjed, on_delete=models.CASCADE)

    # Note: the value is from starting caluclating time, not the start course time
    start_value_time = models.TimeField()

    # Note: the value is at the ending caluclating time, not the end course time
    end_value_time = models.TimeField()

    def __str__(self) -> str:
        return self.name


class Master(models.Model):

    name = models.CharField(max_length=511)

    courses = models.ManyToManyField(Course)

    def __str__(self) -> str:
        return self.name


class CourseComing(models.Model):

    master = models.ForeignKey(Master, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.master} ({self.created_at})"