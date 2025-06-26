document.addEventListener("DOMContentLoaded", () => {

    document.getElementById('form').addEventListener('submit', async function (e) {
        e.preventDefault(); // Stop the form from submitting the traditional way

        const form = e.target;
        const formData = new FormData(form);
        console.log(formData);
        const pathParts = window.location.pathname.split('/'); // we split the url
        const keyword = pathParts[1];

        fetch('/api/' + keyword, {
            method: 'POST',
            body: formData
        })
            .then(response => {
                return response.json();
            })
            .then(result => {
                console.log('Success:', result);
                window.location.href = '/' + keyword + '/' + result.id;
            })
    });
});