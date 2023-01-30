import logging
import os
from datetime import datetime

from utils.elasticsearch import load_in_es
from utils import log
DATA_PATH = os.path.join(os.getcwd(), 'sample_data')
SECRETS_PATH = os.path.join(os.getcwd(), 'secrets')
CAUTH_ID = 'cauths'
CONT_ID = 'conts'
BIDDER_ID = 'bidders'
TENDER_ID = 'tenders'


def main():
    # Date related to the current operation day
    op_date = datetime.now().strftime("%Y%m%d")
    data_path = os.path.join(DATA_PATH, '20220625')

    # Declare project paths
    cauths_path = os.path.join(data_path, CAUTH_ID)
    conts_path = os.path.join(data_path, CONT_ID)
    bidders_path = os.path.join(data_path, BIDDER_ID)
    tenders_path = os.path.join(data_path, TENDER_ID)

    # Load to ES
    load_in_es(
        (
            (os.path.join(cauths_path, CAUTH_ID + '.jsonl'), CAUTH_ID),
            (os.path.join(conts_path, CONT_ID + '.jsonl'), CONT_ID),
            (os.path.join(bidders_path, BIDDER_ID + '.jsonl'), BIDDER_ID),
            (os.path.join(tenders_path, TENDER_ID + '.jsonl'), TENDER_ID),
        )
        , SECRETS_PATH
    )


if __name__ == "__main__":
    main()
