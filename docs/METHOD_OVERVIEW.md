# Method overview

For \(s_i=2x_i-1\), the competitive uncentered prior is

\[
\log p_I(s|h,\alpha,G)=C+\sum_i h_i s_i-\alpha\sum_{\{i,j\}\in E}s_i s_j.
\]

Its binary-space representation is

\[
C'+2\sum_i(h_i+\alpha d_i)x_i
-4\alpha\sum_{\{i,j\}\in E}x_i x_j.
\]

The conditional posterior log odds are

\[
\Delta\ell_i+2h_i+2\alpha d_i-4\alpha\sum_{j\in N(i)}x_j.
\]

The degree correction is

\[
h_i^{corr}=h_i-\alpha d_i,
\]

giving

\[
\Delta\ell_i+2h_i-4\alpha\sum_{j\in N(i)}x_j.
\]

The edge-randomized / degree-redistributed control preserves edge count, not
the original node-degree sequence. A k-regular graph removes between-node
degree heterogeneity but retains a common unary contribution and active
pairwise graph coupling.
