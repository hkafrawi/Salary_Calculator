// Existing function for the original page
function runSalaryFunction() {
    const salaryInput = document.getElementById('salaryInput').value;
    makeAjaxRequest('/calculate-salary', salaryInput, displayResults);
}

// New function for the "Net Salary Simulator" page
function runNetSalaryFunction() {
    const netSalaryInput = document.getElementById('netSalaryInput').value;
    makeAjaxRequest('/net-salary', netSalaryInput, displayResults);
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

// Callback function to display results
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


function navigateToNetSalarySimulator() {
    // Redirect to the "net_salary_simulator" page
    window.location.href = '/net_salary_simulator';
}

function navigateToIndex() {
    // Redirect to the "index" page
    window.location.href = '/';
}