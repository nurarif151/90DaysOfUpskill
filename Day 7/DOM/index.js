<script>
  // Select the title element
  var title = document.getElementById("title");

  // Change the text of the title element
  title.innerHTML = "Coverlater Content Writing";

  // Select the intro section
  var intro = document.getElementById("intro");

  // Add a new paragraph to the intro section
  var newParagraph = document.createElement("p");
  newParagraph.innerHTML = "Our team of talented writers are dedicated to delivering high-quality, engaging content for your audience.";
  intro.appendChild(newParagraph);

  // Select the contact button
  var contactButton = document.getElementById("contact-button");

  // Add a click event to the contact button
  contactButton.addEventListener("click", function() {
    alert("Thank you for your interest in our services! A representative will be in touch with you shortly.");
  });
</script>
