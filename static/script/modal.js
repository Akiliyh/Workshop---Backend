document.addEventListener("DOMContentLoaded", () => {

    function entrance() {
        let modalContainer = document.querySelector('.modal-container');
        let modal = document.querySelector('.modal');
        modal.classList.remove('exit');
        modal.classList.add('entrance');
        modalContainer.classList.add('show');
        modalContainer.style.display = 'inline';
    }

    document.getElementById("modal-btn").addEventListener("click", async () => {entrance()});

    function exit() {
        let modalContainer = document.querySelector('.modal-container');
        let modal = document.querySelector('.modal');
        modal.classList.remove('entrance');
        modal.classList.add('exit');
        modalContainer.classList.remove('show');
        setTimeout(() => {
            modalContainer.style.display = 'none';
        }, 1000);
    }

    document.querySelector(".modal-container").addEventListener("click", async () => { exit() });
    document.getElementById("cancel-btn").addEventListener("click", async () => { exit() });

    document.querySelector(".modal").addEventListener("click", (e) => {
        e.stopPropagation();
    });
})