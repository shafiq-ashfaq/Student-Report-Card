from faker import Faker
fake = Faker()
import random
from .models import *
from django.db.models import Q



def create_subject_marks(n):
    
        stds = Student.objects.all()
        for std in stds:
            subjects = Subject.objects.all()
            for subject in subjects:
                    try:
                        SubjectMarks.objects.create(
                                student = std,
                                subject = subject,
                                marks = random.randint(0,100)


                            )
                    except Exception as e:
                       continue    

def seed_db(n) -> None:
    
     for i in range(0,n):
        try:
            dept_obj = Department.objects.all()
            random_index = random.randint(0, len(dept_obj)-1)
            department = dept_obj[random_index]
            student_id = f"{department}-0{random.randint(100,999)}"
            student_name = fake.name()
            student_email = fake.email()
            student_age = random.randint(18,30)
            student_address = fake.address()

            
            
            

            std_id = StudentID.objects.create(student_id = student_id)
            

            if not Student.objects.filter(Q(student_email = student_email) &  Q(student_id__student_id = std_id)).exists():

                std_obj = Student.objects.create(
                    
                            department = department ,
                            student_id = std_id,
                            student_name = student_name,
                            student_email = student_email, 
                            student_age =   student_age,
                            student_address = student_address,
                )
        except Exception as e:
            continue    




      
    


