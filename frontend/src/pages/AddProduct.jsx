import axios from 'axios';
import React, { useState } from 'react';

export default function AddProduct() {
  const [productName, setProductName] = useState('');
  const [productType, setProductType] = useState('');
  const [price, setPrice] = useState('');
  const [mainStore, setMainStore] = useState('');

  const handleSubmit = (event) => {
    event.preventDefault();
    const newProduct = {
      name: productName,
      type: productType,
      price: price,
      mainStore: mainStore,
    };

    axios
      .post('http://127.0.0.1:8000/products', newProduct)
      .then((response) => {
        console.log('Product added successfully:', response.data);
      })
      .catch((error) => {
        console.error('Error adding product:', error);
      });
  };

  return (
    <form onSubmit={handleSubmit}>
      <div className="card">
        <h2>AFFILIATE WITH US</h2>
        <div className="mb-3">
          <input
            type="text"
            className="form-control"
            id="Product-name"
            placeholder="Product name"
            value={productName}
            onChange={(event) => setProductName(event.target.value)}
            required
          />
        </div>
        <div className="mb-3">
          <input
            type="text"
            className="form-control"
            id="Product-type"
            placeholder="Product type"
            value={productType}
            onChange={(event) => setProductType(event.target.value)}
            required
          />
        </div>
        <div className="mb-3">
          <input
            type="text"
            className="form-control"
            id="Price"
            placeholder="Price"
            value={price}
            onChange={(event) => setPrice(event.target.value)}
            required
          />
        </div>
        <div className="mb-3">
          <input
            type="text"
            className="form-control"
            id="main-store"
            placeholder="main store"
            value={mainStore}
            onChange={(event) => setMainStore(event.target.value)}
            required
          />
        </div>
        <button type="submit" className="btn btn-primary">
          Submit
        </button>
      </div>
    </form>
  );
}