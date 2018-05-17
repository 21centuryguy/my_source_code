var mysql = require('mysql');

var con = mysql.createConnection({
  host: "localhost",
  user: "root",
  password: "tlove759",
  database: "mydb"
});

con.connect(function(err) {
  if (err) throw err;
  console.log("Connected!");
 // var sql = "CREATE TABLE products (name VARCHAR(255))";
 var sql = "INSERT INTO products (name) VALUES ?";
 var values = [
   ['Chocolate Heaven'],
   ['Tasty Lemons'],
   ['Vanilla Dreams'],
  ];
 // con.query(sql, function (err, result) {
   // if (err) throw err;
   // console.log("Table created"); 
  con.query(sql, [values], function (err, result) {
   if (err) throw err;
   console.log("Number of records inserted: " + result.affectedRows);
  });
});
