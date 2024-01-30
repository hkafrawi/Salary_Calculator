// Existing function for the original page
function runSalaryFunction() {
    const salaryInput = document.getElementById('salaryInput').value;
    makeAjaxRequest('/calculate-salary', salaryInput, displayResults);
}

// New function for the "Net Salary Simulator" page
function runNetSalaryFunction() {
    const netSalaryInput = document.getElementById('netSalaryInput').value;
    const grossSalary = find_gross_salary(netSalaryInput);
    makeAjaxRequest('/calculate-salary', grossSalary, displayNetSalaryResults);
}

// Function to simulate calculating gross salary based on net salary
function find_gross_salary(netSalary) {
    // Replace this with your logic to calculate gross salary based on net salary
    // For now, let's assume a simple calculation (gross = net + 100)
    return parseFloat(netSalary) + 100;
}

// Common function to make AJAX requests
function makeAjaxRequest(url, data, callback) {
    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ salary: data }),
    })
    .then(response => response.json())
    .then(callback)
    .catch(error => {
        console.error('Error:', error);
    });
}

// Callback function to display results on the original page
function displayResults(data) {
    if (data.error) {
        console.error('Error:', data.error);
    } else {
        document.getElementById('grossSalary').innerText = `Gross Salary: ${data[0].toFixed(2)}`;
        document.getElementById('employeeShare').innerText = `Employee Share: ${data[1].toFixed(2)}`;
        document.getElementById('ownerShare').innerText = `Owner Share: ${data[2].toFixed(2)}`;
        document.getElementById('taxes').innerText = `Taxes: ${data[3].toFixed(2)}`;
        document.getElementById('netSalary').innerText = `Net Salary: ${data[4].toFixed(2)}`;
    }
}

// Callback function to display results on the "Net Salary Simulator" page
function displayNetSalaryResults(data) {
    if (data.error) {
        console.error('Error:', data.error);
    } else {
        document.getElementById('netGrossSalary').innerText = `Gross Salary: ${data[0].toFixed(2)}`;
        document.getElementById('netEmployeeShare').innerText = `Employee Share: ${data[1].toFixed(2)}`;
        document.getElementById('netOwnerShare').innerText = `Owner Share: ${data[2].toFixed(2)}`;
        document.getElementById('netTaxes').innerText = `Taxes: ${data[3].toFixed(2)}`;
        document.getElementById('netNetSalary').innerText = `Net Salary: ${data[4].toFixed(2)}`;
    }
}
