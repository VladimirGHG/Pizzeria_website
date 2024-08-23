function buttonClicked(formType) {
    var pizzaForm = document.getElementById('pizza');
    var burgerForm = document.getElementById('burger');

    pizzaForm.classList.add('hidden');
    burgerForm.classList.add('hidden');

    if (formType === 'pizza') {
        pizzaForm.classList.remove('hidden');
    } else if (formType === 'burger') {
        burgerForm.classList.remove('hidden');
    }
}