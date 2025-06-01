document.addEventListener("DOMContentLoaded", function () {
    const typeField = document.getElementById("id_type");
    const categoryField = document.getElementById("id_category");
    const subcategoryField = document.getElementById("id_subcategory");

    function filterCategories(preserveSelected = true) {
        const selectedType = typeField.value;
        let preservedValue = categoryField.value;

        Array.from(categoryField.options).forEach(option => {
            const typeId = option.dataset.typeId;
            option.hidden = !!typeId && typeId !== selectedType;
        });

        if (!preserveSelected || !preservedValue || categoryField.querySelector(`option[value="${preservedValue}"]`)?.hidden) {
            categoryField.value = "";
        }

        filterSubcategories(preserveSelected);
    }

    function filterSubcategories(preserveSelected = true) {
        const selectedCategory = categoryField.value;
        const selectedType = typeField.value;
        let preservedValue = subcategoryField.value;

        Array.from(subcategoryField.options).forEach(option => {
            const catId = option.dataset.categoryId;
            const typeId = option.dataset.typeId;
            option.hidden = !(catId === selectedCategory && typeId === selectedType);
        });

        if (!preserveSelected || !preservedValue || subcategoryField.querySelector(`option[value="${preservedValue}"]`)?.hidden) {
            subcategoryField.value = "";
        }
    }

    if (typeField && categoryField && subcategoryField) {
        typeField.addEventListener("change", () => filterCategories(false));
        categoryField.addEventListener("change", () => filterSubcategories(false));

        filterCategories(true);
    }
});
