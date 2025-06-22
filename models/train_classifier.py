from pathlib import Path
import pandas as pd
import fasttext

# Path to save the trained model
MODEL_PATH = Path("models/amharic_title_ft.bin")

def prepare_fasttext_format(df: pd.DataFrame, tmp_path: Path):
    """
    Convert the product title column into FastText training format:
    __label__<label> <title>
    """
    # For now we use a dummy label: __label__product
    lines = [f"__label__product {title.strip()}" for title in df["title"]]
    tmp_path.write_text("\n".join(lines), encoding="utf-8")

def train_and_save(df: pd.DataFrame):
    """
    Train a FastText supervised classifier and save the model.
    """
    tmp = Path("/tmp/ft_train.txt")
    prepare_fasttext_format(df, tmp)

    model = fasttext.train_supervised(
        input=str(tmp),
        epoch=5,
        lr=1.0,
        dim=100,
        wordNgrams=2,
        loss="softmax"
    )

    MODEL_PATH.parent.mkdir(parents=True, exist_ok=True)
    model.save_model(str(MODEL_PATH))
    print(f"[MODEL] FastText model saved → {MODEL_PATH}")
