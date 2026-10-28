"""Online auction system with safer input handling and validation."""

import json
from datetime import datetime
from html import escape

MIN_INCREMENT = 100
BUYER_PREMIUM = 1.05
DATE_FORMAT = "%Y-%m-%d %H:%M"


class Auction:
    """Represent an auction and its bids."""

    def __init__(self, title, seller, reserve_price, ends_at):
        """Initialize an auction."""
        self.title = title
        self.seller = seller
        self.reserve_price = reserve_price
        self.ends_at = datetime.strptime(ends_at, DATE_FORMAT)
        self.bids = []
        self.highest = 0
        self.leader = None

    def place_bid(self, bidder, amount, at):
        """Validate and record a bid."""
        bid_time = datetime.strptime(at, DATE_FORMAT)

        if bid_time > self.ends_at:
            return False
        if bidder == self.seller:
            return False
        if amount < self.reserve_price:
            return False
        if self.highest and amount < self.highest + MIN_INCREMENT:
            return False

        self.bids.append((bidder, amount, at))
        self.highest = amount
        self.leader = bidder
        return True

    def winner(self):
        """Return the winning bidder, if one exists."""
        return self.leader

    def final_price(self):
        """Return the final price including the buyer premium."""
        if self.winner() is None:
            return 0
        return round(self.highest * BUYER_PREMIUM, 2)


auctions = {}


def create_auction(item_id, title, seller, reserve_price, ends_at):
    """Create and store an auction."""
    if item_id in auctions:
        raise ValueError("Auction ID already exists")
    auction = Auction(title, seller, reserve_price, ends_at)
    auctions[item_id] = auction
    return auction


def bid(item_id, bidder, amount, at):
    """Place a bid and return False for an unknown auction."""
    auction = auctions.get(item_id)
    if auction is None:
        return False
    try:
        return auction.place_bid(bidder, amount, at)
    except ValueError:
        return False


def top_bidders(item_id, n=3):
    """Return unique bidders ordered by their highest bid."""
    auction = auctions.get(item_id)
    if auction is None:
        return []
    highest_bids = {}
    for bidder, amount, _ in auction.bids:
        highest_bids[bidder] = max(amount, highest_bids.get(bidder, 0))
    return sorted(
        highest_bids,
        key=highest_bids.get,
        reverse=True,
    )[:n]


def render_listing(item_id):
    """Render a safely escaped HTML listing."""
    auction = auctions[item_id]
    title = escape(auction.title)
    return (
        f"<h2>{title}</h2>"
        f"<p>Current bid: Rs.{auction.highest}</p>"
    )


def bidder_badge(name):
    """Render a bidder badge with escaped text."""
    return f"<span class='bidder'>{escape(str(name))}</span>"


def export_bids(item_id):
    """Export auction bids as JSON."""
    auction = auctions[item_id]
    rows = [
        {"bidder": bidder, "amount": amount, "at": at}
        for bidder, amount, at in auction.bids
    ]
    return json.dumps(rows)


def seconds_left(item_id):
    """Return seconds remaining until the auction closes."""
    auction = auctions[item_id]
    return int((auction.ends_at - datetime.now()).total_seconds())


def main():
    """Run a demonstration of auction validation."""
    create_auction(
        "LOT1", "Vintage Camera", "seller_sam", 5000,
        "2026-12-01 18:00",
    )
    create_auction(
        "LOT2", "<script>alert('pwned')</script>Old Radio",
        "seller_ria", 2000, "2026-12-01 18:00",
    )
    create_auction(
        "LOT3", "Brass Lamp", "seller_ria", 800,
        "2026-12-01 18:00",
    )

    print("Asha bids 5000:", bid("LOT1", "asha", 5000, "2026-12-01 10:00"))
    print("Ben bids 5100:", bid("LOT1", "ben", 5100, "2026-12-01 10:05"))
    print("Seller bids on own item:", bid(
        "LOT1", "seller_sam", 6000, "2026-12-01 11:00"
    ))
    print("Winner:", auctions["LOT1"].winner())
    print("Final price:", auctions["LOT1"].final_price())
    print("Top bidders:", top_bidders("LOT1"))
    print("Zero bid:", bid("LOT3", "carl", 0, "2026-12-01 11:30"))
    print("Safe listing:", render_listing("LOT2"))
    print("Safe badge:", bidder_badge("<img src=x onerror=alert(1)>"))


if __name__ == "__main__":
    main()
