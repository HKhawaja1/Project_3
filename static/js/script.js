// Meal Section Toggling
document.addEventListener('DOMContentLoaded', function() {
    // Get all the buttons and sections
    const buttons = document.querySelectorAll('.toggle-button');
    const sections = document.querySelectorAll('.menu-section');
  
    // Add event listener to each button
    buttons.forEach(button => {
      button.addEventListener('click', () => {
        // Get the section corresponding to the button
        const section = document.getElementById(button.getAttribute('data-section'));
  
        // Hide all sections first
        sections.forEach(sec => sec.classList.remove('active'));
  
        // Show the selected section by adding the 'active' class
        section.classList.add('active');
      });
    });
  
    // By default, show the 'veggie' section on page load
    document.getElementById('veggie').classList.add('active');
  });
  
  // FAQ Section Toggling
  document.querySelectorAll('.faq-question').forEach((item) => {
    item.addEventListener('click', () => {
      const parent = item.parentElement;
      parent.classList.toggle('active');
      item.classList.toggle('active');
    });
  });
  