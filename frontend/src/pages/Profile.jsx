export default function Profile(){
    return(
        <form>
     <div  className="card"> 
        <h2>AFFILIATE WITH US</h2>     
       <div class="mb-3">
          <input type="text" class="form-control" id="Product-name" placeholder="FULL NAMES"required></input>
        </div>
         <div class="mb-3">
          <input type="email" class="form-control" id="email" placeholder="EMAIL"required></input>
        </div>
        <div class="mb-3">
          <input type="text" class="form-control" id="Price" placeholder="COMPANY NAME"required></input>
        </div>
        <div class="mb-3">
          <input type="password" class="form-control" id="password" placeholder="PASSWORD" required></input>
        </div>
        <button type="submit" class="btn btn-primary">Submit</button>
        </div>
      </form>
      
    )
}