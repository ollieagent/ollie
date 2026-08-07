import Lake
open Lake DSL

package «ollie» where
  leanVersion := "v4.12.0"

require mathlib from git
  "https://github.com/leanprover-community/mathlib4" @ "v4.12.0"

@[default_target]
lean_lib Ollie where
