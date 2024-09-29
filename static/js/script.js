// Smooth Scroll to Top Script
document.addEventListener('DOMContentLoaded', function() {
	const footerLogo = document.getElementById('footer-logo');
	footerLogo.addEventListener('click', function() {
		window.scrollTo({
			top: 0,
			behavior: 'smooth'
		});
	});
});

// Meal Section Toggling
document.addEventListener('DOMContentLoaded', function() {
	const buttons = document.querySelectorAll('.toggle-button');
	const sections = document.querySelectorAll('.menu-section');

	buttons.forEach(button => {
		button.addEventListener('click', () => {
			const section = document.getElementById(button.getAttribute('data-section'));
			sections.forEach(sec => sec.classList.remove('active'));
			section.classList.add('active');
		});
	});

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

// jQuery Hover Effect for Cards
$(document).ready(function() {
	$('.meal-plan-card, .menu-card').hover(
		function() {
			$(this).css({
				'box-shadow': '0 8px 16px rgba(0, 0, 0, 0.2)',
				'transform': 'scale(1.05)',
				'transition': 'transform 0.3s ease, box-shadow 0.3s ease'
			});
		},
		function() {
			$(this).css({
				'box-shadow': 'none',
				'transform': 'scale(1)',
				'transition': 'transform 0.3s ease, box-shadow 0.3s ease'
			});
		}
	);
});