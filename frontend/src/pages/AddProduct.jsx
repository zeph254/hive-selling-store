export default function AddProduct(){
    return(
        <form>
     <div  className="card"> 
        <h2>AFFILIATE WITH US</h2>     
       <div class="mb-3">
          <input type="text" class="form-control" id="Product-name" placeholder="Product name"required></input>
        </div>
         <div class="mb-3">
          <input type="text" class="form-control" id="Product-type" placeholder="Product type"required></input>
        </div>
        <div class="mb-3">
          <input type="text" class="form-control" id="Price" placeholder="Price"required></input>
        </div>
        <div class="mb-3">
          <input type="text" class="form-control" id="main-store" placeholder="main store" required></input>
        </div>
        <button type="submit" class="btn btn-primary">Submit</button>
        </div>
      </form>
      
    )
}