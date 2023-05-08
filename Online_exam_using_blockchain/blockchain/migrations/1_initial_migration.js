const Migrations = artifacts.require("Structresult");

module.exports = function (deployer) {
  deployer.deploy(Migrations);
};
