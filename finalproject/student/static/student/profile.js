document.addEventListener('DOMContentLoaded', function () {
    // Change between links
    const enquiryButton = document.getElementById('profile-enquiries');
    const propertyButton = document.getElementById('profile-properties');
    const editButton = document.getElementById('profile-edit');
    const enquiryContent = document.getElementById('enquiries');
    const propertyContent = document.getElementById('properties');
    const editContent = document.getElementById('edit');
    const acceptButton = document.querySelectorAll('#Confirmed')
    const declineButton = document.querySelectorAll('#Declined')
    const buttonFinished = document.querySelectorAll('.button-finished')
    enquiryButton.addEventListener('click', () => {
        // Show content
        enquiryContent.style.display = 'block';
        propertyContent.style.display = 'none';
        editContent.style.display = 'none';
        // Change text color
        enquiryButton.style.color = '#000';
        propertyButton.style.color = '#8b8b8b';
        editButton.style.color = '#8b8b8b';
    });
    propertyButton.addEventListener('click', () => {
        // Show content
        enquiryContent.style.display = 'none';
        propertyContent.style.display = 'block';
        editContent.style.display = 'none';
        // Change text color
        enquiryButton.style.color = '#8b8b8b';
        propertyButton.style.color = '#000';
        editButton.style.color = '#8b8b8b';
    });
    editButton.addEventListener('click', () => {
        // Show content
        enquiryContent.style.display = 'none';
        propertyContent.style.display = 'none';
        editContent.style.display = 'block';
        // Change text color
        enquiryButton.style.color = '#8b8b8b';
        propertyButton.style.color = '#8b8b8b';
        editButton.style.color = '#000';
    });

    acceptButton.forEach(accept => {
        accept.addEventListener('click', () => {
            const booking_id = accept.getAttribute("data-id");
            const decline = document.querySelector(`.Declined-${booking_id}`);
            const finished = document.querySelector(`.Finished-${booking_id}`);
            decline.style.display = 'none';
            accept.style.display = 'none';
            finished.style.display = 'block';
            finished.style.backgroundColor = '#3bc518';
            finished.innerHTML = 'Confirmed';
            fetch ("/accept", {
                method: "POST",
                body: JSON.stringify({
                    booking_id: booking_id,
                }),
            });
        });
    });

    declineButton.forEach(decline => {
        decline.addEventListener('click', () => {
            const booking_id = decline.getAttribute("data-id");
            const accept = document.querySelector(`.Confirmed-${booking_id}`);
            const finished = document.querySelector(`.Finished-${booking_id}`);
            decline.style.display = 'none';
            accept.style.display = 'none';
            finished.style.display = 'block';
            finished.style.backgroundColor = '#e62020';
            finished.innerHTML = 'Declined';
            fetch ("/decline", {
                method: "POST",
                body: JSON.stringify({
                    booking_id: booking_id,
                }),
            });
        });
    });
});
