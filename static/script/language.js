document.addEventListener("DOMContentLoaded", () => {
    document.getElementById("delete-btn").addEventListener("click", async () => {
        const poiId = poiData.id;
        fetch('/api/language/' + poiId, {
            method: 'DELETE',
        }).then(res => res.text())
            .then(res => {
                console.log("Delete success:", res);
                window.location.href = "/";
            })
    });
});