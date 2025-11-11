import marimo

__generated_with = "0.17.7"
app = marimo.App(width="medium")


@app.cell
def _(mo):
    mo.md(r"""
    # インタラクティブなスライダーを作成し、サイン波の周波数を変更しながらリアルタイムに描画
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## スライダーの作成
    """)
    return


@app.cell
def _():
    import marimo as mo

    slider = mo.ui.slider(1, 10, value=5, label="周波数")
    slider
    return mo, slider


@app.cell
def _(mo):
    mo.md(r"""
    ##　スライダーの値に応じて描画
    """)
    return


@app.cell
def _(slider):
    import numpy as np
    import matplotlib.pyplot as plt

    freq = slider.value

    x = np.linspace(0, 2 * np.pi, 500)
    y = np.sin(freq * x)

    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.set_title(f"sin({freq}x)")
    ax.grid(True)
    fig
    return


if __name__ == "__main__":
    app.run()
