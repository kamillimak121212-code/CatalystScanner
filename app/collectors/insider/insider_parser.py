import xml.etree.ElementTree as ET

from app.collectors.insider.insider_models import (
    InsiderTransaction
)

from app.collectors.insider.transaction_codes import (
    TRANSACTION_CODES
)


def _get_text(root, path):

    element = root.find(path)

    if element is None:
        return ""

    if element.text is None:
        return ""

    return element.text.strip()


def parse_form4(company, xml_text):

    root = ET.fromstring(xml_text)

    transaction = InsiderTransaction()

    transaction.ticker = company.ticker

    transaction.insider = _get_text(
        root,
        ".//rptOwnerName"
    )

    if transaction.insider == "":
        return None

    # ----------------------------------------------------
    # ROLE
    # ----------------------------------------------------

    roles = []

    if _get_text(root, ".//isDirector") == "1":
        roles.append("Director")

    if _get_text(root, ".//isOfficer") == "1":
        roles.append("Officer")

    if _get_text(root, ".//isTenPercentOwner") == "1":
        roles.append("10% Owner")

    if _get_text(root, ".//isOther") == "1":

        other = _get_text(root, ".//otherText")

        if other:
            roles.append(other)
        else:
            roles.append("Other")

    transaction.role = ", ".join(roles)

    # ----------------------------------------------------
    # TRANSACTION
    # ----------------------------------------------------

    transaction.transaction_code = _get_text(
        root,
        ".//transactionCode"
    )

    transaction.transaction_type = TRANSACTION_CODES.get(
        transaction.transaction_code,
        "Unknown"
    )

    transaction.transaction_date = _get_text(
        root,
        ".//transactionDate/value"
    )

    # ----------------------------------------------------
    # SHARES
    # ----------------------------------------------------

    shares = _get_text(
        root,
        ".//transactionShares/value"
    )

    if shares:
        transaction.shares = float(shares)

    price = _get_text(
        root,
        ".//transactionPricePerShare/value"
    )

    if price:
        transaction.price = float(price)

    transaction.transaction_value = (
        transaction.shares *
        transaction.price
    )

    # ----------------------------------------------------
    # AFTER TRANSACTION
    # ----------------------------------------------------

    shares_after = _get_text(
        root,
        ".//sharesOwnedFollowingTransaction/value"
    )

    if shares_after:
        transaction.shares_after = float(shares_after)

    transaction.ownership = _get_text(
        root,
        ".//directOrIndirectOwnership/value"
    )

    # ----------------------------------------------------
    # FOOTNOTE
    # ----------------------------------------------------

    transaction.footnote = _get_text(
        root,
        ".//footnote"
    )

    return transaction