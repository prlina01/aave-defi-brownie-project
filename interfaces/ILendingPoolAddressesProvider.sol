// SPDX-License-Identifier: MIT

pragma solidity ^0.6.6;

contract ILendingPoolAddressesProvider {
    function getLendingPool() external view returns (address);
}
