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
        fetch ("/accept", {
            method: "POST",
            body: JSON.stringify({
                booking_id: booking_id
            }),
        });
        });
    });

    declineButton.forEach(decline => {
        decline.addEventListener('click', () => {
        console.log('declined')
        })
    });
});
