pragma solidity >=0.5.0 <0.9.0;

// Creating a Smart Contract
contract Structresult{

struct result{
	// State variables
	uint bid;
	string stid;
	string  subid;
	string  mark;
	string date;
	

}
result []emps;

function addmark(uint bid, string memory stid,string memory subid,string memory mark,string memory date) public{
	result memory e =result(bid,stid,subid,mark,date);
	emps.push(e);
}

}
