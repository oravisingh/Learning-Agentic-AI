from pydantic import BaseModel, computed_field, Field

# TODO: Create Booking model
# Fields:
# -user_id: int
# -room_id: int
# -night: int (must be >= 1)
# -rate_per_night: float
# Also, add computed field: total_amount = night*rate_per_night


class Booking(BaseModel):
    user_id: int
    room_id: int
    night: int = Field(
        ...,
        ge = 1
    )
    rate_per_night: float 

    @computed_field
    @property
    def total_amount(self) -> float:
        return self.night * self.rate_per_night