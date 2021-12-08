document.addEventListener('DOMContentLoaded', function () {
    likeButton = document.querySelectorAll(".like_button")
    likeButton.forEach((element) => {
        element.addEventListener("click", () => {
            const id = element.getAttribute("data-id");
            let likesCount = document.querySelector(`#likes-${id}`);
            if (element.className == "like_button bi bi-heart-fill") {
                element.className = "like_button bi bi-heart";
                likesCount.innerHTML = parseInt(likesCount.innerHTML) - 1;
            } else if (element.className == "like_button bi bi-heart") {
                element.className = "like_button bi bi-heart-fill";
                likesCount.innerHTML = parseInt(likesCount.innerHTML) + 1;
            }
            fetch ("/like", {
                method: "POST",
                body: JSON.stringify({
                    post_id: id,
                }),
            });
        });
    });
})