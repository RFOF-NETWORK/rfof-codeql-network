/**
 * @name RFOF Python Strict Security Rule
 * @description Erzwingt globale Sicherheitsstandards im Python-Monolithen.
 * @kind problem
 * @security-severity 8.0
 * @precision high
 * @id rfof/python/strict-security
 * @tags security
 */

import python

from Call c
where c.getAnArg().toString().matches("%eval%") or c.getAnArg().toString().matches("%exec%")
select c, "RFOF WARNING: Unsafe code execution (eval/exec) detected in the decentralized monolith!"
