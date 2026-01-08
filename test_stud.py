# Import the grade calculation function from main program
from studentdetails import calculate_average, assign_grade

# ---------------- GRADE S TEST CASES ----------------

# Test lower boundary for Grade S (exactly 90)
def test_grade_S_lower_boundary():
    avg = calculate_average(90,90,90)
    assert assign_grade(avg) == "S"

# Test middle value for Grade S
def test_grade_S_middle_value():
    avg = calculate_average(95, 95, 95)
    assert assign_grade(avg) == "S"

# Test upper boundary for Grade S (exactly 100)
def test_grade_S_upper_boundary():
    avg = calculate_average(100, 100, 100)
    assert assign_grade(avg) == "S"

# ---------------- GRADE A TEST CASES ----------------

# Test lower boundary for Grade A (exactly 80)
def test_grade_A_lower_boundary():
    avg = calculate_average(80, 80, 80)
    assert assign_grade(avg) == "A"

    
# Test middle value for Grade A
def test_grade_A_middle_value():
    avg = calculate_average(85, 85, 85)
    assert assign_grade(avg) == "A"


# Test upper boundary just below 90
def test_grade_A_upper_boundary():
    avg = calculate_average(89.99, 89.99, 89.99)
    assert assign_grade(avg) == "A"

    

# ---------------- GRADE B TEST CASES ----------------

# Test lower boundary for Grade B (exactly 65)
def test_grade_B_lower_boundary():
   avg = calculate_average(65, 65, 65)
   assert assign_grade(avg) == "B"


# Test middle value for Grade B
def test_grade_B_middle_value():
    avg = calculate_average(72, 72, 72)
    assert assign_grade(avg) == "B"


# Test upper boundary just below 80
def test_grade_B_upper_boundary():
    avg = calculate_average(79.99, 79.99, 79.99)
    assert assign_grade(avg) == "B"


# ---------------- GRADE C TEST CASES ----------------

# Test lower boundary for Grade C (exactly 50)
def test_grade_C_lower_boundary():
    avg = calculate_average(50, 50, 50)
    assert assign_grade(avg) == "C"


# Test middle value for Grade C
def test_grade_C_middle_value():
    avg = calculate_average(58, 58, 58)
    assert assign_grade(avg) == "C"



# Test upper boundary just below 65
def test_grade_C_upper_boundary():
    avg = calculate_average(64.99, 64.99, 64.99)
    assert assign_grade(avg) == "C"


# ---------------- GRADE D TEST CASES ----------------

# Test lower boundary for Grade D (exactly 40)
def test_grade_D_lower_boundary():
    avg = calculate_average(40, 40, 40)
    assert assign_grade(avg) == "D"

# Test middle value for Grade D
def test_grade_D_middle_value():
    avg = calculate_average(45, 45, 45)
    assert assign_grade(avg) == "D"
    
# Test upper boundary just below 50
def test_grade_D_upper_boundary():
    avg = calculate_average(49.99, 49.99, 49.99)
    assert assign_grade(avg) == "D"
    

# ---------------- GRADE F TEST CASES ----------------

# Test value below 40 should return Grade F
def test_grade_F_below_40():
    avg = calculate_average(30, 30, 30)
    assert assign_grade(avg) == "F"