def calculate_cgpa():
    print("CGPA Calculator")
    total_credits = int(input("Enter the total number of credits: "))
    total_grade_points = 0
    for i in range(total_credits):
        grade_point = float(input(f"Enter the grade point for credit {i + 1}: "))
        total_grade_points += grade_point
    cgpa = total_grade_points / total_credits
    print(f"Your CGPA is: {cgpa:.2f}")

if __name__ == "__main__":
    calculate_cgpa()

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CGPA Calculator</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 20px; }
        .container { max-width: 500px; margin: auto; padding: 20px; border: 1px solid #ddd; border-radius: 8px; }
        h2 { color: #333; }
        input, button { padding: 8px; margin: 5px 0; width: 100%; }
        button { cursor: pointer; }
        .result { margin-top: 10px; font-weight: bold; }
    </style>
</head>
<body>
    <div class="container">
        <h1>CGPA Calculator</h1>
        <label for="total-credits">Total Number of Credits:</label>
        <input type="number" id="total-credits" min="1" step="1">
        <div id="cgpa-credits"></div>
        <button onclick="calculateCgpa()">Calculate CGPA</button>
        <div id="cgpa-result" class="result"></div>
    </div>

    <script>
        function calculateCgpa() {
            const totalCredits = parseInt(document.getElementById('total-credits').value);
            if (isNaN(totalCredits) || totalCredits <= 0) {
                alert('Please enter a valid number of credits.');
                return;
            }
            
            let totalGradePoints = 0;
            for (let i = 0; i < totalCredits; i++) {
                const gradePoint = parseFloat(prompt(`Enter the grade point for credit ${i + 1}:`));
                if (isNaN(gradePoint)) {
                    alert('Invalid grade point input. Please enter a number.');
                    return;
                }
                totalGradePoints += gradePoint;
            }
            
            const cgpa = totalGradePoints / totalCredits;
            document.getElementById('cgpa-result').textContent = `Your CGPA is: ${cgpa.toFixed(2)}`;
        }
    </script>
</body>
</html>
