function Transactions({ data }: any) {
  const listTrans = data.map((item: any, index: any) => (
    <div key={index}>
      <div className="list-group">
        <a
          href="#"
          className="list-group-item list-group-item-action flex-column align-items-start"
        >
          <div className="d-flex w-100 justify-content-between">
            <h5 className="mb-1">
              {index + 1} : {item.Desc}
            </h5>
            <small>Amount : {item.Amount}</small>
          </div>
        </a>
      </div>
    </div>
  ));
  return <ul>{listTrans}</ul>;
}

export default Transactions;
