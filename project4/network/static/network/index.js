document.addEventListener('DOMContentLoaded', function () {
    const followButton = document.querySelector('.followButton')
    const followersCount = document.querySelector('#followersCount')
    followButton?.addEventListener('click', () => {
        if (followButton.innerHTML == 'Follow') {
            followButton.innerHTML = 'Following';
            followButton.style.color = '#000000';
            followButton.style.borderColor = '#000000';
            let newCount = parseInt(followersCount.innerHTML) + 1;
            followersCount.innerHTML = newCount;
        } else {
            followButton.innerHTML = 'Follow';
            followButton.style.color = '#000000';
            followButton.style.borderColor = '#000000';
            let newCount = parseInt(followersCount.innerHTML) - 1;
            followersCount.innerHTML = newCount;
        }
        // Post request to follow/unfollow
        const user = document.querySelector('.profileUsername').innerHTML;
        fetch(`/${user}/follow`, {
            method: "POST",
          })
    });
    followButton?.addEventListener('mouseover', () =>  {
        if (followButton.innerHTML == 'Following') {
            followButton.innerHTML = 'Unfollow';
            followButton.style.color = '#f4212E';
            followButton.style.borderColor = '#f4212E';
        }
    });
    followButton?.addEventListener('mouseout', () =>  {
        if (followButton.innerHTML == 'Unfollow') {
            followButton.innerHTML = 'Following';
            followButton.style.color = '#000000';
            followButton.style.borderColor = '#000000';
        }
    });
});




