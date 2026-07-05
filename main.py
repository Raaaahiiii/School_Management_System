from school import School 
from person import Student,Teacher
from subject import Subject 
from classroom import ClassRoom

school= School("XYZ","DHAKA")
       
       #adding clsrooms
eight= ClassRoom("Eight")
nine= ClassRoom("Nine")
ten= ClassRoom("Ten")
school.add_classroom(eight)
school.add_classroom(nine)
school.add_classroom(ten)

       #adding stds
rahi= Student("Rahi",eight)
mahi= Student("Mahi",nine)
fahi= Student("Fahi",ten)
bahi= Student("Bahi",ten)

school.student_addmission(rahi)
school.student_addmission(mahi)
school.student_addmission(fahi)
school.student_addmission(bahi)
       #adding teacher
abul= Teacher("Abul Babu")
babul= Teacher("Babul Babu")
kabul= Teacher("Kabul Hai")
       #adding sub with teacher
bangla= Subject("Bangla",abul)
physics= Subject("Physics",babul)
chemistry= Subject("Chemistry",kabul)
biology= Subject("Biology",kabul)

eight.add_subject(bangla)
eight.add_subject(physics)
eight.add_subject(chemistry)
nine.add_subject(biology)
nine.add_subject(physics)
nine.add_subject(chemistry)
ten.add_subject(bangla)
ten.add_subject(physics)
ten.add_subject(chemistry)
ten.add_subject(biology)

eight.take_semester_final_exam()
nine.take_semester_final_exam()
ten.take_semester_final_exam()

print(school)

