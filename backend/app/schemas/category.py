from pydantic import BaseModel, Field


class CategoryBase(BaseModel):
    name: str = Fiend(..., min_lenght = 5, max_lenght = 100,description = "Category name")
    slug: str = Fiend(..., min_lenght = 5, max_lenght = 100,description = "URL-friendly Category name")

class CategoryCreate(CategoryBase):
    pass

class CategoryResponse(CategoryBase):
    id: int = Field(..., description = "Unique category identifier")

    class Config:
        form_attributes = True