async function runFlow() {
    const name = document.getElementById("name").value;
    const response = await fetch('/run-flow', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ name })
    });
    const data = await response.json();
    document.getElementById("result").innerText = data.result[0]["id"];
}
