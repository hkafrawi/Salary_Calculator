function runSalaryFunction() {
    const salaryInput = document.getElementById('salaryInput').value;

    // Make an AJAX request to the server (you may use fetch or another library like axios)
    // Assume the server endpoint is /calculate-salary and it returns JSON data
    fetch('/calculate-salary', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ salary: salaryInput }),
    })
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            console.log('Data received:', data);
            console.error('Error:', data.error);
        } else {
            // Update the result container with the calculated values
            console.log('Data received:', data);
            document.getElementById('grossSalary').innerText = `Gross Salary: ${data[0]}`;
            document.getElementById('employeeShare').innerText = `Employee Share: ${data[1]}`;
            document.getElementById('ownerShare').innerText = `Owner Share: ${data[2]}`;
            document.getElementById('taxes').innerText = `Taxes: ${data[3]}`;
            document.getElementById('netSalary').innerText = `Net Salary: ${data[4]}`;
        }
    })
    .catch(error => {
        console.error('Error:', error);
    })
}
