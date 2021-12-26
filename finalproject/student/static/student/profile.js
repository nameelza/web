document.addEventListener("DOMContentLoaded", function () {
  // Change between links
  const enquiryButton = document.getElementById("profile-enquiries");
  const propertyButton = document.getElementById("profile-properties");
  const editButton = document.getElementById("profile-edit");
  const enquiryContent = document.getElementById("enquiries");
  const propertyContent = document.getElementById("properties");
  const editContent = document.getElementById("edit");
  const acceptButton = document.querySelectorAll("#Confirmed");
  const declineButton = document.querySelectorAll("#Declined");
  const firstNameButton = document.querySelector("#first-change");
  const lastNameButton = document.querySelector("#last-change");
  const emailButton = document.querySelector("#email-change");
  enquiryButton.addEventListener("click", () => {
    // Show content
    enquiryContent.style.display = "block";
    propertyContent.style.display = "none";
    editContent.style.display = "none";
    // Change text color
    enquiryButton.style.color = "#000";
    propertyButton.style.color = "#8b8b8b";
    editButton.style.color = "#8b8b8b";
  });
  propertyButton.addEventListener("click", () => {
    // Show content
    enquiryContent.style.display = "none";
    propertyContent.style.display = "block";
    editContent.style.display = "none";
    // Change text color
    enquiryButton.style.color = "#8b8b8b";
    propertyButton.style.color = "#000";
    editButton.style.color = "#8b8b8b";
  });
  editButton.addEventListener("click", () => {
    // Show content
    enquiryContent.style.display = "none";
    propertyContent.style.display = "none";
    editContent.style.display = "block";
    // Change text color
    enquiryButton.style.color = "#8b8b8b";
    propertyButton.style.color = "#8b8b8b";
    editButton.style.color = "#000";
  });

  acceptButton.forEach((accept) => {
    accept.addEventListener("click", () => {
      const booking_id = accept.getAttribute("data-id");
      const decline = document.querySelector(`.Declined-${booking_id}`);
      const finished = document.querySelector(`.Finished-${booking_id}`);
      decline.style.display = "none";
      accept.style.display = "none";
      finished.style.display = "block";
      finished.style.backgroundColor = "#3bc518";
      finished.innerHTML = "Confirmed";
      fetch("/accept", {
        method: "POST",
        body: JSON.stringify({
          booking_id: booking_id,
        }),
      });
    });
  });

  declineButton.forEach((decline) => {
    decline.addEventListener("click", () => {
      const booking_id = decline.getAttribute("data-id");
      const accept = document.querySelector(`.Confirmed-${booking_id}`);
      const finished = document.querySelector(`.Finished-${booking_id}`);
      decline.style.display = "none";
      accept.style.display = "none";
      finished.style.display = "block";
      finished.style.backgroundColor = "#e62020";
      finished.innerHTML = "Declined";
      fetch("/decline", {
        method: "POST",
        body: JSON.stringify({
          booking_id: booking_id,
        }),
      });
    });
  });

  firstNameButton.addEventListener("click", (event) => {
    first_name = document.querySelector("#first_name").value;
    fetch("/profile_edit", {
      method: "POST",
      body: JSON.stringify({
        action: "first_name",
        first_name,
      }),
    });
    const message = document.querySelector("#success-first");
    message.style.display = "block";
    event.preventDefault();
  });

  lastNameButton.addEventListener("click", (event) => {
    last_name = document.querySelector("#last_name").value;
    fetch("/profile_edit", {
      method: "POST",
      body: JSON.stringify({
        action: "last_name",
        last_name,
      }),
    });
    const message = document.querySelector("#success-last");
    message.style.display = "block";
    event.preventDefault();
  });

  emailButton.addEventListener("click", (event) => {
    email = document.querySelector("#email").value;
    fetch("/profile_edit", {
      method: "POST",
      body: JSON.stringify({
        action: "email",
        email,
      }),
    });
    const message = document.querySelector("#success-email");
    message.style.display = "block";
    event.preventDefault();
  });
});
