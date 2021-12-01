document.addEventListener('DOMContentLoaded', function () {
    document.querySelector('.follow').addEventListener('click', () => {
        if (document.querySelector('.follow').innerHTML == 'Follow') {
            document.querySelector('.follow').innerHTML = 'Following';
        } else {
            document.querySelector('.follow').innerHTML = 'Follow';
        }
    });
    document.querySelector('.follow').addEventListener('mouseover', () =>  {
        console.log('mouseover');
        if (document.querySelector('.follow').innerHTML == 'Following') {
            document.querySelector('.follow').innerHTML = 'Unfollow';
        }
    });
    document.querySelector('.follow').addEventListener('mouseout', () =>  {
        console.log('mouseout');
        if (document.querySelector('.follow').innerHTML == 'Unfollow') {
            document.querySelector('.follow').innerHTML = 'Following';
        }
    });
});




