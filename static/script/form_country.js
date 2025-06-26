document.addEventListener("DOMContentLoaded", () => {

    document.getElementById('form').addEventListener('submit', async function(e) {
    e.preventDefault(); // Stop the form from submitting the traditional way

    const form = e.target;
    const formData = new FormData(form);
    console.log(formData);

    fetch('/api/country', {
        method: 'POST',
        body: formData
    })
    .then(response => {
        return response.json();
    })
    .then(result => {
        console.log('Success:', result);
        window.location.href = '/country/' + result.id;
    })
});
});