document.addEventListener("DOMContentLoaded", () => {
    document.getElementById("init-btn").addEventListener("click", async () => {
        fetch('/api/init', {
            method: 'PUT',
        }).then(res => res.text())
            .then(res => {
                console.log("Reinitiated all the database:", res);
                window.location.reload();
            })
    });
});