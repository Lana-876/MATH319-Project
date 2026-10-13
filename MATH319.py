from datetime import datetime
import hashlib 
import secrets

#قاعدة البيانات المؤقتة لتخزين الهاشات وحالة الاستخدام
 database = {}
# توليد الرمز العشوائي وحفظ الهاش 
def make_token():
    token = secrets.token_hex(16)
    token_hash = hashlib.sha256(token.encode()).hexdigest()
    database[token_hash] = False  
  
    return token
#داله التحقق من الرمز ومنع التكرار
def check_use(token):
  token_hash = hashlib.sha256(token.encode()).hexdigest()
   #الرمز غير موجود 
    if token_hash not in database:
        return False 
   # الرمز تم استخدامه
    if database[token_hash] : 
        return False
   # الرمز لم يستخدم + يحدث حالته
    database[token_hash] = True
        return True

# List of students who can vote
valid_students = ["461210292", "461208099", "461210122",
                  "45281743", "45102948"]

def student_interface():

    # Check the voting deadline
    deadline = datetime(2026, 12, 5, 23, 59, 59)
    now = datetime.now()

    if now > deadline:
        print("Voting time is over.")
        return
    
    print("============================")
    print("Welcome to the voting system")

    # Enter student ID with retry loop
    while True:
        student_id = input("Enter your student ID (or type 'exit' to quit): ")
        if student_id.lower() == 'exit':
            return
        if student_id in valid_students:
            break
        print("Student ID is not valid. Please try again.")

    # Show the candidates
    print("\nChoose your candidate:")
    print("1. Lana Alarefe")
    print("2. Layan Alharbi")
    print("3. Amal Almutairi")

    while True:
        choice = input("Enter your choice: ")

        # Check the selected candidate
        if choice == "1":
            candidate = "Lana Alarefe"
            break
        elif choice == "2":
            candidate = "Layan Alharbi"
            break
        elif choice == "3":
            candidate = "Amal Almutairi"
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 3.")

    # At this stage: DO NOT store student ID (belongs to student 2)

  

    # Just confirm the vote selection
    print("Your vote has been recorded (token will be handled by student 2).")
    print("You voted for:", candidate)


# Run the program
if __name__ == "__main__":
    student_interface()
    
