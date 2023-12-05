// Define the array of products 


const products = [
    {
        Name: "Product A",
        ShortDescription: "Used for general purpose",
        LongDescription: "Description of Product A. This is a placeholder text for the long description of the product.",
        ImageURL: "/static/sample_webpage/images/ProductA.jpg",
    },
    {
        Name: "Product B",
        ShortDescription: "Used for general purpose",
        LongDescription: "Description of Product B. This is a placeholder text for the long description of the product.",
        ImageURL: "/static/sample_webpage/images/ProductB.jpg",
    },
    {
        Name: "Product C",
        ShortDescription: "Used for general purpose",
        LongDescription: "Description of Product C. This is a placeholder text for the long description of the product.",
        ImageURL: "/static/sample_webpage/images/ProductC.jpg",
    },
    {
        Name: "Product D",
        ShortDescription: "Used for general purpose",
        LongDescription: "Description of Product D. This is a placeholder text for the long description of the product.",
        ImageURL: "/static/sample_webpage/images/ProductD.jpg",
    },
    {
        Name: "Product E",
        ShortDescription: "Used for general purpose",
        LongDescription: "Description of Product E. This is a placeholder text for the long description of the product.",
        ImageURL: "/static/sample_webpage/images/ProductE.jpg",
    },
    {
        Name: "Product F",
        ShortDescription: "Used for general purpose",
        LongDescription: "Description of Product F. This is a placeholder text for the long description of the product.",
        ImageURL: "/static/sample_webpage/images/ProductF.jpg",
    },
    {
        Name: "Product G",
        ShortDescription: "Used for general purpose",
        LongDescription: "Description of Product G. This is a placeholder text for the long description of the product.",
        ImageURL: "/static/sample_webpage/images/ProductG.jpg",
    },
    {
        Name: "Product H",
        ShortDescription: "Used for general purpose",
        LongDescription: "Description of Product H. This is a placeholder text for the long description of the product.",
        ImageURL: "/static/sample_webpage/images/ProductH.jpg",
    },
    // Add more product objects here
];



// Function to create and display products
function displayProducts() {
    const productsContainer = document.getElementById("productsContainer");

    // Loop through the products array
    products.forEach(product => {
        const productDiv = document.createElement("div");
        productDiv.classList.add("product");

        const productName = document.createElement("h2");
        productName.textContent = product.Name;

        const shortDescription = document.createElement("p");
        shortDescription.textContent = product.ShortDescription;

        const longDescription = document.createElement("p");
        longDescription.textContent = product.LongDescription;

        productDiv.appendChild(productName);

        // Check if ShortDescription is provided and not an empty string
        if (product.ShortDescription && product.ShortDescription.trim() !== "") {
            const shortDescription = document.createElement("p");
            shortDescription.textContent = product.ShortDescription;
            productDiv.appendChild(shortDescription);
        }

        // Check if LongDescription is provided and not an empty string
        if (product.LongDescription && product.LongDescription.trim() !== "") {
            const longDescription = document.createElement("p");
            longDescription.textContent = product.LongDescription;
            productDiv.appendChild(longDescription);
        }

        // Check if ImageURL is provided
        // Create an <img> element with an onerror event
        if (product.ImageURL) {
            const productImage = document.createElement("img");
            productImage.alt = "Product Image";
            productImage.title = product.Name; // Add tooltip for the image
            productImage.onerror = function () {
                this.src = "/static/sample_webpage/images/picture-not-available.jpg";
            };
            productImage.src = product.ImageURL;
            productDiv.appendChild(productImage);
        }

        productsContainer.appendChild(productDiv);
        // Add a separator (horizontal rule) between each product
        const separator = document.createElement("hr");
        productsContainer.appendChild(separator);
    });
}

// Call the displayProducts function to display the products
displayProducts();