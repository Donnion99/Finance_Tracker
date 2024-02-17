function Login() {
  let success;

  return (
    <>
      <div className="container">
        <h1>Login</h1>
        {success ? (
          <div className="alert alert-success" role="alert">
            <a href="/login/" className="alert-link">
              Click here to login
            </a>
            .
          </div>
        ) : (
          ""
        )}

        <form method="post" action="/login/">
          <br />
          <div className="mb-3">
            <label htmlFor="exampleInputEmail1" className="form-label">
              Email address
            </label>
            <input
              name="user"
              type="email"
              className="form-control"
              id="exampleInputEmail1"
              aria-describedby="emailHelp"
            />
          </div>
          <div className="mb-3">
            <label htmlFor="exampleInputPassword1" className="form-label">
              Password
            </label>
            <input
              name="pass"
              type="password"
              className="form-control"
              id="exampleInputPassword1"
            />
          </div>
          <button type="submit" className="btn btn-primary">
            Log in
          </button>
        </form>
      </div>
    </>
  );
}

export default Login;
